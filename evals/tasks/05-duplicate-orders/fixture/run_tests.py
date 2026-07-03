from report import build_report, total_billed

lines = build_report()

assert any(line[1] == 103 for line in lines)
assert any(line[1] == 104 for line in lines)
assert all(len(line) == 3 for line in lines)
assert total_billed() > 0

print("visible tests passed")
