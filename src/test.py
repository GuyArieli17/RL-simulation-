import cityflow
eng = cityflow.Engine('json/config.json')
for i in range(1000):
    if i == 50:
        eng.set_tl_phase("intersection_0_0", 1)
    eng.next_step()
print(eng.get_current_time())

