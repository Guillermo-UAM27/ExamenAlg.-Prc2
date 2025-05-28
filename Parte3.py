from datetime import date
from typing import List, Optional


class Prescription:
    
    def __init__(self, medication: str, dosage: str, instructions: str, issued_on: Optional[date] = None):
        self.medication = medication
        self.dosage = dosage
        self.instructions = instructions
        self.issued_on = issued_on or date.today()

    def __repr__(self):
        return (
            f"Receta(medicamento={self.medication}, dosis={self.dosage}, "
            f"instrucciones={self.instructions}, fecha={self.issued_on.isoformat()})"
        )


class Patient:
    
    def __init__(self, patient_id: int, name: str):
        self.id = patient_id
        self.name = name
        self._stack: List[Prescription] = []  # Pila LIFO de recetas

    def add_prescription(self, prescription: Prescription) -> None:
        self._stack.append(prescription)
        print(f"→ Receta agregada: {prescription}")

    def peek_last_prescription(self) -> Optional[Prescription]:
        
        if not self._stack:
            print("No hay recetas en el historial.")
            return None
        last = self._stack[-1]
        print(f"→ Última receta (tope de la pila): {last}")
        return last

    def get_history(self) -> List[Prescription]:
       
        return list(self._stack)


def main():
    print("=== Gestión de Historial de Recetas ===")
    try:
        pid = int(input("Ingrese ID del paciente: "))
    except ValueError:
        print("ID inválido. Saliendo.")
        return
    name = input("Ingrese nombre del paciente: ").strip()

    patient = Patient(pid, name)
    print(f"Paciente creado: {patient.name} (ID {patient.id})")

    while True:
        print("\nOpciones:")
        print("  1) Agregar receta")
        print("  2) Ver última receta")
        print("  3) Ver historial completo")
        print("  4) Salir")
        choice = input("Elija opción (1-4): ").strip()

        if choice == '1':
            med = input("  Medicamento: ").strip()
            dose = input("  Dosis: ").strip()
            instr = input("  Instrucciones: ").strip()
            rec = Prescription(med, dose, instr)
            patient.add_prescription(rec)

        elif choice == '2':
            patient.peek_last_prescription()

        elif choice == '3':
            history = patient.get_history()
            if not history:
                print("No hay recetas registradas.")
            else:
                print("Historial completo de recetas (de viejo a nuevo):")
                for idx, r in enumerate(history, 1):
                    print(f"  {idx}. {r}")

        elif choice == '4':
            print("Saliendo...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
