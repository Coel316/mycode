list1 = ["apple", 33, {"potAYto": "potAHto", "tomAYto":"tomAHto"}]

for item in list1:
    try:
        plusone = item + 1
        print(plusone)
        import fakename
    except TypeError as terr:
        print(terr, "oophs! Couldn't do that.")
    except Exception as err
        print("Hmmm.. something else went wrong."
    finally:
        print("All done")

