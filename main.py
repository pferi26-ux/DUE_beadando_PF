import tkinter as tk
from tkinter import ttk, messagebox
import PF_back as api
from PF_logo_draw import pf_draw_logo

class ServiceGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("App - Jármú következő szervíz nyilváltartó")


        self.api = api.ServiceClient()
        pf_draw_logo(self.master)

        self.tree = ttk.Treeview(master, columns=("jarmu", "tulaj", "km"), show="headings")
        self.tree.heading("jarmu", text="Jármű")
        self.tree.heading("tulaj", text="Tulajdonos")
        self.tree.heading("km", text="Következő olajcsere (km)")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


        frame = tk.Frame(master)
        frame.pack(pady=5)

        tk.Label(frame, text="Jármű:").grid(row=0, column=0)
        self.entry_vehicle = tk.Entry(frame)
        self.entry_vehicle.grid(row=0, column=1)

        tk.Label(frame, text="Tulajdonos:").grid(row=1, column=0)
        self.entry_owner = tk.Entry(frame)
        self.entry_owner.grid(row=1, column=1)

        tk.Label(frame, text="Következő olajcsere:").grid(row=2, column=0)
        self.entry_km = tk.Entry(frame)
        self.entry_km.grid(row=2, column=1)

        btn_frame = tk.Frame(master)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Hozzáadás", command=self.pf_add_interval).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Törlés", command=self.pf_delete_interval).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Módosítás", command=self.pf_mod_interval).grid(row=0, column=2, padx=10)

        self.pf_load_intervals()


    def pf_load_intervals(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        try:
            intervals = self.api.pf_list_intervals()
            for i in intervals:
                self.tree.insert("", tk.END, iid=i["id"], values=(i["vehicle"], i["owner"], i["interval_km"]))
        except Exception as e:
            messagebox.showerror("Hiba", f"Nem sikerült lekérdezni az adatokat:\n{e}")

    def pf_add_interval(self):
        vehicle = self.entry_vehicle.get()
        owner = self.entry_owner.get()
        try:
            km = int(self.entry_km.get())
        except ValueError:
            messagebox.showerror("Hiba", "Az intervallumnak számnak kell lennie!")
            return

        if not vehicle or not owner:
            messagebox.showerror("Hiba", "Minden mezőt ki kell tölteni!")
            return

        try:
            self.api.pf_add_interval(vehicle, owner, km)
            self.pf_load_intervals()
            self.entry_vehicle.delete(0, tk.END)
            self.entry_owner.delete(0, tk.END)
            self.entry_km.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Hiba", f"Nem sikerült hozzáadni:\n{e}")


    def pf_mod_interval(self):
        selected = self.tree.selection()
        vehicle = self.entry_vehicle.get()
        owner = self.entry_owner.get()
        if not selected:
            messagebox.showwarning("Figyelem", "Válassz ki egy elemet a módosításhoz!")
            return
        if vehicle or owner:
            messagebox.showerror("Hiba", "Csak a kilométert adja meg!!")
            return

        sid = int(selected[0])

        try:
            km = int(self.entry_km.get())
            self.api.pf_mod_interval(sid,km)
            self.pf_load_intervals()
        except ValueError:
            messagebox.showerror("Hiba", "Az intervallumnak számnak kell lennie!")
            return
        except Exception as e:
            messagebox.showerror("Hiba", f"Nem sikerült módosítani:\n{e}")

    def pf_delete_interval(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Figyelem", "Válassz ki egy elemet a törléshez!")
            return

        sid = int(selected[0])

        try:
            self.api.pf_delete_interval(sid)
            self.pf_load_intervals()
        except Exception as e:
            messagebox.showerror("Hiba", f"Nem sikerült törölni:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = ServiceGUI(root)
    root.mainloop()