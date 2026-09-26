Soongsil, Korea, Hanyang = map(int, input().split())
if Soongsil + Korea + Hanyang >= 100:
    print("OK")
else:
    if Soongsil == min(Soongsil, Korea, Hanyang):
        print("Soongsil")
    elif Korea == min(Soongsil, Korea, Hanyang):
        print("Korea")
    elif Hanyang == min(Soongsil, Korea, Hanyang):
        print("Hanyang")