from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # para invocarlo: python manage.py importar_sucursales_desde_csv datos/sucursalescsv.csv (ojo no lleva .py)
    help = (
        "Este programa se usa para importar usuarios desde un archivo CSV local. "
        "Espera columnas: codigo_sucursal,nombre_sucursal"
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
        from ...forms import Sucursal_Form

        if self.verbosity >= self.NORMAL:
            self.stdout.write("=== Importando sucursales ===")

        with open(self.file_path, mode="r") as f:
            reader = csv.DictReader(f)
            for index, row_dict in enumerate(reader):
                form = Sucursal_Form(data=row_dict)
                if form.is_valid():
                    sucursal = form.save()
                    if self.verbosity >= self.NORMAL:
                        self.stdout.write( f"{row_dict['codigo_sucursal']} - {row_dict['nombre_sucursal']}:\n" )                        
                        #self.stdout.write(f" - {sucursal}\n")
                    self.imported_counter += 1
                else:
                    if self.verbosity >= self.NORMAL:
                        self.stderr.write( f"Errores importando sucursal " f"{row_dict['codigo_sucursal']} - {row_dict['nombre_sucursal']}:\n" )
                        self.stderr.write(f"{form.errors.as_json()}\n")
                    self.skipped_counter += 1
  
    def finalize(self):
      if self.verbosity >= self.NORMAL:
          self.stdout.write(f"-------------------------\n")
          self.stdout.write(f"Sucursales importadas: {self.imported_counter}\n")
          self.stdout.write(f"Sucursales ignoradas: {self.skipped_counter}\n\n")