from typing import List, DictS
# Se refactoriza la clase para mejorar legibilidad, mantenibilidad
# y cumplimiento de buenas prácticas de calidad de software.
class LibroDiario:
    """
    Clase que gestiona las transacciones contables de ingresos y egresos.
    """

    def __init__(self) -> None:
        """
        Inicializa el libro diario con una lista vacía de transacciones.
        """
        self.transacciones: List[Dict[str, object]] = []

    def agregar_transaccion(
        self, fecha: str, descripcion: str, monto: float, tipo: str
    ) -> None:
        """
        Agrega una transacción al libro diario.

        :param fecha: Fecha de la transacción
        :param descripcion: Descripción del movimiento
        :param monto: Valor monetario positivo
        :param tipo: Tipo de transacción ('ingreso' o 'egreso')
        """

        # Validación del tipo de transacción
        if tipo not in ("ingreso", "egreso"):
            raise ValueError("El tipo de transacción debe ser 'ingreso' o 'egreso'")

        # Validación del monto
        if monto <= 0:
            raise ValueError("El monto debe ser un valor positivo")

        self.transacciones.append(
            {
                "fecha": fecha,
                "descripcion": descripcion,
                "monto": monto,
                "tipo": tipo,
            }
        )

    def calcular_resumen(self) -> Dict[str, float]:
        """
        Calcula el total de ingresos y egresos.

        :return: Diccionario con los totales calculados
        """

        ingresos: float = 0.0
        egresos: float = 0.0

        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                ingresos += float(transaccion["monto"])
            else:
                egresos += float(transaccion["monto"])

        # Se retorna una estructura de datos, no texto formateado
        return {
            "ingresos": ingresos,
            "egresos": egresos,
        }
