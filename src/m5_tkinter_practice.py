"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Nathalie Grier.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """

    window = tkinter.Tk()

    frame1 = ttk.Frame(window, padding=30)
    frame1.grid()

    what_todo_button = ttk.Button(frame1, text='What to do?')
    what_todo_button['command'] = (lambda: to_do())
    what_todo_button.grid()

    print_hello_button = ttk.Button(frame1, text='Hello')
    print_hello_button['command'] = (lambda: print('Hello'))
    print_hello_button.grid()

    entry_box = ttk.Entry(frame1)
    entry_box.grid()
    chance_entry_box = ttk.Button(frame1, text='Chance')
    chance_entry_box['command'] = (lambda: hello_goodbye(entry_box))
    chance_entry_box.grid()

    new_entry_box = ttk.Entry(frame1)
    new_entry_box.grid()
    print_new = ttk.Button(frame1, text='Print Entry')
    print_new['command'] = (lambda: number(new_entry_box, entry_box))
    print_new.grid()

    window.mainloop()

def hello_goodbye(entry_box):
    ok = 'ok'
    if entry_box.get() == ok:
        print('Hello')
    else:
        print('Goodbye')

def number(new, old):
    num = int(new.get())
    print(old.get() * num)

def to_do():
    print('Press Hello to print the word Hello')
    print('Type in the first box and press Chance, try to get the response Goodbye.')
    print('Type a string in the first box and an integer in the second box, press Print Entry.')

    # -------------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################

    # -------------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
