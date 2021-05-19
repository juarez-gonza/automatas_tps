def fmain(t, reporter, input_m, **input_kwarg):
    inp = input_m.take_input(**input_kwarg)
    t.init_tape(inp)
    status = t.run()
    reporter.gen_log()
    return status
