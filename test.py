import pymol

# Inisialisasi PyMOL
pymol.finish_launching()

# Muat file PDB atau CIF protein
pymol.cmd.load("1fat.pdb", "protein")

# Tambahkan representasi
pymol.cmd.show("cartoon", "protein")
pymol.cmd.show("sticks", "ligand")

# Posisi tampilan dan pencahayaan
pymol.cmd.zoom()
pymol.cmd.turn("x", 180)

# Menampilkan tampilan PyMOL
pymol.cmd.png("protein_visualization.png", width=800, height=600, dpi=300, ray=1)

# Tutup sesi PyMOL
pymol.cmd.quit()