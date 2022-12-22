import sqlite3
import tkinter
from tkinter import RIGHT, Y, LEFT, BOTH, VERTICAL, ttk

import customtkinter


def league_button_function():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.title("Leagues")
    root.geometry("500x200")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    conn = sqlite3.connect('leagues.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT LeagueName, NumTeamsInLeague, LeagueId FROM League''')
    records = cur.fetchall()
    league_name_label = customtkinter.CTkLabel(frame, text="LEAGUE NAME")
    league_name_label.grid(row=1, column=1)
    num_teams_label = customtkinter.CTkLabel(frame, text="NUMBER OF TEAMS")
    num_teams_label.grid(row=1, column=4)
    i = 0
    for record in records:
        league_label = customtkinter.CTkButton(frame, text=record[0],
                                               command=lambda record=record: league_teams_button_function(
                                                   str(record[2])))
        league_label.grid(row=i + 2, column=1)
        league_label = customtkinter.CTkLabel(frame, text=record[1])
        league_label.grid(row=i + 2, column=4)
        i = i + 1

    conn.commit()
    conn.close()

    root.mainloop()


def league_teams_button_function(league_id):
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.title("Teams")
    root.geometry("500x500")
    second_frame = scrollbar(root)

    conn = sqlite3.connect('leagues.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT TeamName, StateName from Teams JOIN State USING (StateID) WHERE LeagueID = ''' + league_id +
                ' ORDER BY TeamName')
    records = cur.fetchall()
    team_name_label = customtkinter.CTkLabel(second_frame, text="TEAM NAME")
    team_name_label.grid(row=1, column=1)
    state_label = customtkinter.CTkLabel(second_frame, text="STATE")
    state_label.grid(row=1, column=8)
    i = 0
    for record in records:
        team_label = customtkinter.CTkLabel(second_frame, text=record[0])
        team_label.grid(row=i + 2, column=1)
        state_name_label = customtkinter.CTkLabel(second_frame, text=record[1])
        state_name_label.grid(row=i + 2, column=8)
        i = i + 1

    conn.commit()
    conn.close()
    root.mainloop()


def states_button_function(equality_check, order_statement):
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.title("States")
    root.geometry("500x500")
    second_frame = scrollbar(root)

    conn = sqlite3.connect('leagues.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT StateName, NumTeamsInState, StateID From State
                WHERE NumTeamsInState ''' + equality_check + ''' 0 ''' + order_statement)
    records = cur.fetchall()
    state_label = customtkinter.CTkLabel(second_frame, text="STATE")
    state_label.grid(row=1, column=1)
    num_teams_button = customtkinter.CTkButton(second_frame, text="NUMBER OF TEAMS",
                                               command=lambda:
                                               states_button_function('>', ' ORDER BY NumTeamsInState DESC'))
    num_teams_button.grid(row=1, column=8)
    i = 0
    for record in records:
        state_name_label = customtkinter.CTkButton(second_frame, text=record[0],
                                                   command=lambda record=record: teams_in_state_button(record))
        state_name_label.grid(row=i + 2, column=1)
        num_label = customtkinter.CTkLabel(second_frame, text=record[1])
        num_label.grid(row=i + 2, column=8)
        i = i + 1

    conn.commit()
    conn.close()
    root.mainloop()


def cities_button_function():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.title("Cities With Teams")
    root.geometry("500x500")
    second_frame = scrollbar(root)

    conn = sqlite3.connect('leagues.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT DISTINCT TeamCity, StateName From Teams JOIN State USING (StateId) ORDER BY TeamCity''')
    records = cur.fetchall()
    city_label = customtkinter.CTkLabel(second_frame, text="CITY")
    city_label.grid(row=1, column=1)
    city_label = customtkinter.CTkLabel(second_frame, text="STATE")
    city_label.grid(row=1, column=3)
    i = 0
    for record in records:
        city_name_label = customtkinter.CTkLabel(second_frame, text=record[0])
        city_name_label.grid(row=i + 2, column=1)
        city_label = customtkinter.CTkLabel(second_frame, text=record[1])
        city_label.grid(row=i+2, column=3)
        i = i + 1

    conn.commit()
    conn.close()
    root.mainloop()


def teams_in_state_button(record):
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.title("Leagues")
    root.geometry("500x500")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    conn = sqlite3.connect('leagues.sqlite')
    cur = conn.cursor()
    cur.execute('''SELECT TeamName FROM Teams JOIN State USING (StateID) WHERE StateID = ''' + str(record[2]))
    records = cur.fetchall()
    i = 0
    if len(records) == 0:
        team_label = customtkinter.CTkLabel(frame, text="This state does not have any professional teams.")
        team_label.grid(row=i + 2, column=1)
    for record in records:
        team_label = customtkinter.CTkLabel(frame, text=record[0])
        team_label.grid(row=i + 2, column=1)
        i = i + 1

    conn.commit()
    conn.close()
    root.mainloop()


def scrollbar(root):
    main_frame = tkinter.Frame(root)
    main_frame.pack(fill=BOTH, expand=1)
    my_canvas = tkinter.Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    second_frame = tkinter.Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    return second_frame
