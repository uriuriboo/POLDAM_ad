n1, m1 = map(int, input().split())
print(n1, m1)

origin_vertex = []
for i in range(n1):
    method, id, fh, ph, cfh, cph = input().split()
    mp = {"method": method, "id": id, "fh": fh,
          "ph": ph, "cfh": cfh, "cph": cph}
    origin_vertex.append(mp)
# origin_edge = []
for i in range(m1):
    v1, v2 = map(int, input().split())

target_vertex = []
n2, m2 = map(int, input().split())
for i in range(n2):
    method, id, fh, ph, cfh, cph = input().split()
    mp = {"method": method, "id": id, "fh": fh,
          "ph": ph, "cfh": cfh, "cph": cph}
    target_vertex.append(mp)

for i in range(n1):
    output = ""
    diff = False
    if origin_vertex[i]["fh"] != target_vertex[i]["fh"]:
        output += "FH "
        diff = True
    if origin_vertex[i]["ph"] != target_vertex[i]["ph"]:
        output += "PH "
        diff = True
    if diff == True:
        print(origin_vertex[i]["method"], output)
