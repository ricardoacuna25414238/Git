import json
import os
from datetime import datetime

class GestorTareas:
    def __init__(self):
        self.tareas = []
        self.archivo = "tareas.json"
        self.cargar_tareas()
    
    def cargar_tareas(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, 'r', encoding='utf-8') as f:
                self.tareas = json.load(f)
    
    def guardar_tareas(self):
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump(self.tareas, f, indent=2, ensure_ascii=False)
    
    def agregar_tarea(self, titulo, descripcion=""):
        tarea = {
            'id': len(self.tareas) + 1,
            'titulo': titulo,
            'descripcion': descripcion,
            'estado': 'pendiente',
            'fecha': datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tareas.append(tarea)
        self.guardar_tareas()
        return tarea
    
    def ultima_tarea(self):
        return self.tareas[-1] if self.tareas else None
    
    def listar_tareas(self):
        if not self.tareas:
            print("\n📋 No hay tareas")
            return
        
        print("\n" + "="*50)
        print("📋 MIS TAREAS")
        print("="*50)
        for t in self.tareas:
            estado = "✅" if t['estado'] == 'completada' else "⏳"
            print(f"{estado} [{t['id']}] {t['titulo']}")
            print(f"   📝 {t['descripcion']}")
            print(f"   📅 {t['fecha']}")
            print("-" * 40)
    
    def completar_tarea(self, id_tarea):
        for t in self.tareas:
            if t['id'] == id_tarea:
                t['estado'] = 'completada'
                self.guardar_tareas()
                return True
        return False

def menu():
    gestor = GestorTareas()
    
    while True:
        print("\n" + "="*40)
        print("📋 GESTOR DE TAREAS")
        print("="*40)
        print("1. ➕ Agregar tarea")
        print("2. 📋 Ver todas")
        print("3. 📌 Ver última")
        print("4. ✅ Completar tarea")
        print("5. 🚪 Salir")
        
        opcion = input("\nOpción: ")
        
        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            tarea = gestor.agregar_tarea(titulo, descripcion)
            print(f"✅ Tarea '{titulo}' agregada (ID: {tarea['id']})")
        
        elif opcion == "2":
            gestor.listar_tareas()
        
        elif opcion == "3":
            tarea = gestor.ultima_tarea()
            if tarea:
                print("\n📌 ÚLTIMA TAREA")
                print(f"ID: {tarea['id']}")
                print(f"Título: {tarea['titulo']}")
                print(f"Descripción: {tarea['descripcion']}")
                print(f"Estado: {tarea['estado']}")
                print(f"Fecha: {tarea['fecha']}")
            else:
                print("❌ No hay tareas")
        
        elif opcion == "4":
            gestor.listar_tareas()
            try:
                id_tarea = int(input("\nID a completar: "))
                if gestor.completar_tarea(id_tarea):
                    print("✅ Tarea completada")
                else:
                    print("❌ Tarea no encontrada")
            except ValueError:
                print("❌ ID inválido")
        
        elif opcion == "5":
            print("👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción inválida")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    menu()