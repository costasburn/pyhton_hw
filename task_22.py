def group_by_surname(list_of_enrollees):
    a_i = []
    j_p = []
    q_t = []
    u_z = []
    for i in list_of_enrollees:
        name, surname = i.rsplit()
        if ord(surname[:1]) <= 73:
            a_i.append(i)
        elif ord(surname[:1]) > 73 and ord(surname[:1]) <= 80:
            j_p.append(i)
        elif ord(surname[:1]) > 80 and ord(surname[:1]) <= 84:
            q_t.append(i)
        elif ord(surname[:1]) > 84 and ord(surname[:1]) <= 90:
            u_z.append(i)
    return len(a_i), len(j_p), len(q_t), len(u_z)


list_of_enrollees = ["Rosalie Castaneda", "Leisa Bluhm", "Nan Haymaker", "Laticia Charboneau", "Ada Ovalle", "Felipa Gaynor", "Claire Horvath", "Elfrieda Wrede", "Melani Muma", "Anastacia Mccleskey"]
print(group_by_surname(list_of_enrollees))
