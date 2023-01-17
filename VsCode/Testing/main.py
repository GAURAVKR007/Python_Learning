def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return "Enter a Number"
    except (ValueError,AssertionError) as err:
            return err


        