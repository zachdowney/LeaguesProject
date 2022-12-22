import buttons
import customtkinter


def gui_homepage():
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("dark-blue")
    root = customtkinter.CTk()
    root.title("Leagues Database")
    root.geometry("500x500")

    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    league_button = customtkinter.CTkButton(master=frame, text="View Leagues", command=buttons.league_button_function)
    league_button.pack(pady=12, padx=10)
    team_button = customtkinter.CTkButton(master=frame, text="View All Teams",
                                          command=lambda: buttons.league_teams_button_function('1 or 2 or 3 or 4'))
    team_button.pack(pady=12, padx=10)
    nfl_button = customtkinter.CTkButton(master=frame, text="View All NFL Teams",
                                         command=lambda: buttons.league_teams_button_function('1'))
    nfl_button.pack(pady=12, padx=10)
    nba_button = customtkinter.CTkButton(master=frame, text="View All NBA Teams",
                                         command=lambda: buttons.league_teams_button_function('2'))
    nba_button.pack(pady=12, padx=10)
    mlb_button = customtkinter.CTkButton(master=frame, text="View All MLB Teams",
                                         command=lambda: buttons.league_teams_button_function('3'))
    mlb_button.pack(pady=12, padx=10)
    nhl_button = customtkinter.CTkButton(master=frame, text="View All NHL Teams",
                                         command=lambda: buttons.league_teams_button_function('4'))
    nhl_button.pack(pady=12, padx=10)
    states_with_button = customtkinter.CTkButton(master=frame, text="View States With Teams",
                                                 command=lambda: buttons.states_button_function('>', ''))
    states_with_button.pack(pady=12, padx=10)
    states_without_button = customtkinter.CTkButton(master=frame, text="View All States Without Teams",
                                                    command=lambda: buttons.states_button_function('=', ''))
    states_without_button.pack(pady=12, padx=10)
    city_button = customtkinter.CTkButton(master=frame, text="View All Cities With Teams",
                                          command=buttons.cities_button_function)
    city_button.pack(pady=12, padx=10)

    root.mainloop()
