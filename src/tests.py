# Clase Abstracta Model:
# Crear una clase abstracta llamada Model que actúa como una plantilla para los modelos específicos de la plataforma.
# En esta clase, se añadirá una propiedad llamada path que almacenará la ubicación del archivo JSON asociado a ese modelo.

# Clases Específicas para Modelos:
# Para cada modelo específico de la plataforma (por ejemplo, Room y Booking), se creará una clase que extienda la clase abstracta Model.
# Cada clase específica tendrá su propia propiedad path que apunta al archivo JSON relevante.

# Método 'list' en la Clase Abstracta:
# En la clase abstracta Model, se implementará un método llamado list utilizando el decorador @classmethod.
# Este método utilizará la propiedad path para leer todos los datos del archivo JSON asociado al modelo.

# Argparse en app.py:
# En el archivo app.py, se utilizará el módulo argparse para manejar parámetros desde la línea de comandos.
# Se definirá un parámetro llamado 'action', que representará la operación que se desea realizar (por ejemplo, 'read-rooms').

# Llamada de Métodos Apropiados:
# Dependiendo del valor del parámetro 'action', se llamará al método apropiado en las clases específicas.
# Por ejemplo, si 'action' es 'read-rooms', se llamará a Room.list().

# Métodos Adicionales en Clase Abstracta:
# Se añadirán métodos adicionales en la clase abstracta Model, como view, delete, create, y update, utilizando decoradores @classmethod y @abstractmethod.
# view utilizará el archivo de lista para buscar un objeto, delete no hará nada por ahora, y create y update serán métodos abstractos.

# Implementación de 'create' y 'update' en Clases Específicas:
# En las clases específicas (Room y Booking), se implementarán los métodos abstractos create y update.
# Estos métodos solicitarán información al usuario a través de input, formarán un diccionario con los datos y, por ahora, simplemente imprimirán esos datos.

# Ejecución desde app.py:
# Al ejecutar app.py desde la línea de comandos con el parámetro 'action', se realizará la operación correspondiente según la lógica implementada.