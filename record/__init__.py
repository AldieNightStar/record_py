def record_init(g, l):
	global _gs
	global _ls
	_gs = g
	_ls = l

def record(name, *args, **kv):
	# Args with assignments to "self."
	sb = []
	for a in args:
		sb.append("self." + a + " = " + a)
	argsStr = "\n\t\t".join(sb)
	# Args separated by comma
	argsCommaSep = ", ".join(args)
	# Printable args
	sb = []
	for a in args:
		sb.append(f"'{a}: ' + str(self.{a}) + '; '")
	concatSelfArgs = " + ".join(sb)
	extString = ""
	if kv.get("extends") != None:
		extString = "(" + kv.get("extends").__name__ + ")"
	# Output
	out= f"""class {name}{extString}:
	def __init__(self, {argsCommaSep}):
		{argsStr}
	def __repr__(self):
		return "{name}(" + {concatSelfArgs} + ")"

"""
	exec(out, _gs, _ls)