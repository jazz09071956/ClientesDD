from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """
    # para invocarlo: python manage.py importar_giros_negocio_desde_csv datos/giros_negocio_csv.csv (ojo no lleva .py) el ambiente virtual debe estar activo, si hay problemas con el set de caracteres abrirlo con la opcionde origen de datos de excel y cuando asigne el correcto volverlo a guardar un set que funcia es el 1252 - western european (windows)
    """
    help = (
        "Este programa se usa para importar giros de negocio desde un archivo CSV local. "
        "Espera columnas: codigo_giro_negocio,nombre_giro_negocio"
        " Sin espacios despues de la coma ni en la cabecera ni en los datos."

    )
    SILENT, NORMAL, VERBOSE, VERY_VERBOSE = 0, 1, 2, 3

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("file_path", nargs=1, type=str)

    def handle(self, *args, **options):
        self.verbosity = options.get("verbosity", self.NORMAL)
        self.file_path = options["file_path"][0]
        self.prepare()
        self.main()
        self.finalize()

    def prepare(self):
        self.imported_counter = 0
        self.skipped_counter = 0

    def main(self):
        import csv
        from ...forms import Giro_Negocio_Form

        if self.verbosity >= self.NORMAL:
            self.stdout.write("=== Importando giros de negocio ===")

        with open(self.file_path, mode="r") as f:
            reader = csv.DictReader(f)
            for index, row_dict in enumerate(reader):
                form = Giro_Negocio_Form(data=row_dict)
                if form.is_valid():
                    giro_negocio = form.save()
                    if self.verbosity >= self.NORMAL:
                        self.stdout.write( f"{row_dict['codigo_giro_negocio']} - {row_dict['nombre_giro_negocio']}:\n" )                        
                        #self.stdout.write(f" - {giro_negocio}\n")
                    self.imported_counter += 1
                else:
                    if self.verbosity >= self.NORMAL:
                        self.stderr.write( f"Errores importando giro_negocio " f"{row_dict['codigo_giro_negocio']} - {row_dict['nombre_giro_negocio']}:\n" )
                        self.stderr.write(f"{form.errors.as_json()}\n")
                    self.skipped_counter += 1
  
    def finalize(self):
      if self.verbosity >= self.NORMAL:
          self.stdout.write(f"-------------------------\n")
          self.stdout.write(f"Giros de Negocio importados: {self.imported_counter}\n")
          self.stdout.write(f"Giros de Negocio ignorados: {self.skipped_counter}\n\n")