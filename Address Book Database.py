from tkinter import *
import sqlite3

root = Tk()
root.title('Python Database')
root.iconbitmap(r'C:\Users\hp\Documents\Experimental Images')
root.geometry("410x500")

conn = sqlite3.connect('address_book.db')
c = conn.cursor()
'''
c.execute(""" CREATE TABLE addresses (
        fname text,
        lname text,
        addresses text,
        city text,
        state text
        )""")
'''


def save():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET 
            fname = :first,
            lname = :last,
            addresses = :address,
            city = :city,
            state = :state

            WHERE _rowid_ = :_rowid_""",
              {'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               '_rowid_': record_id
               })

    conn.commit()
    conn.close()

    editor.destroy()


def update():
    global editor
    editor = Tk()
    editor.title('Update A Record')
    editor.iconbitmap(r'C:\Users\hp\Documents\Experimental Images')
    editor.geometry("400x200")

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("SELECT * FROM addresses WHERE _rowid_ = " + record_id)
    records = c.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    f_name_label = Label(editor, text="First Name", font="Times 10")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name", font="Times 10")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address", font="Times 10")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City", font="Times 10")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State", font="Times 10")
    state_label.grid(row=4, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])

    save_btn = Button(editor, text="Update record", font="Times 10", command=save)
    save_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)


def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("DELETE FROM addresses WHERE _rowid_= " + delete_box.get())

    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get()
              })

    conn.commit()
    conn.close()

    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)


def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute("SELECT *,_rowid_ FROM addresses")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[5]) + "\t" + str(record[0]) + "\t" + str(record[1]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()
    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)
address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)
city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)
state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=10)

f_name_label = Label(root, text="First Name", font="Times 12")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name", font="Times 12")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address", font="Times 12")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City", font="Times 12")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State", font="Times 12")
state_label.grid(row=4, column=0)
delete_box_label = Label(root, text="Select ID", font="Times 12")
delete_box_label.grid(row=9, column=0, pady=10)

submit_btn = Button(root, text="Add record to the database", font="Times 12", command=submit)
submit_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="Show record", font="Times 12", command=query)
query_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_btn = Button(root, text="Delete record", font="Times 12", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

update_btn = Button(root, text="Update record", font="Times 12", command=update)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

conn.commit()
conn.close()

root.mainloop()
