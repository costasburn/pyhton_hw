def group_by_surname(list_of_enrollees):
    a_i = []
    j_p = []
    q_t = []
    u_z = []
    for i in list_of_enrollees:
        name, surname = i.rsplit()
        if ord(surname[:1]) <= ord('I'):
            a_i.append(i)
        elif ord(surname[:1]) > ord('I') and ord(surname[:1]) <= ord('P'):
            j_p.append(i)
        elif ord(surname[:1]) > ord('P') and ord(surname[:1]) <= ord('T'):
            q_t.append(i)
        elif ord(surname[:1]) > ord('T') and ord(surname[:1]) <= ord('Z'):
            u_z.append(i)
    return len(a_i), len(j_p), len(q_t), len(u_z)


list_of_enrollees = ["Rosalie Castaneda", "Leisa Bluhm", "Nan Haymaker", "Laticia Charboneau", "Ada Ovalle", "Felipa Gaynor", "Claire Horvath", "Elfrieda Wrede", "Melani Muma", "Anastacia Mccleskey"]
print(group_by_surname(list_of_enrollees))
