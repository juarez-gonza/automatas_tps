def fmain(t, reporter, input_m):
    inp = input_m.take_input()
    t.init_tape(inp)
    status = t.run()
    reporter.gen_log()
