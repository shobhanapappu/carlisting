import customtkinter as ctk
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import json
import threading
import logging
from datetime import datetime
from config import Config
from automation.musalist_automation import MusalistAutomation


class MainWindow:
    def __init__(self):
        ctk.set_appearance_mode("System")  # Use system theme for better integration
        ctk.set_default_color_theme("blue")  # Modern blue theme
        self.root = ctk.CTk()
        self.root.title("Musalist Automation Suite")
        self.root.geometry("1100x700")  # Slightly larger for better content fit
        self.root.minsize(1000, 650)
        self.automation = MusalistAutomation()
        self.automation.set_gui_callback(self.update_stats)
        self.automation_thread = None
        self.is_running = False
        self.theme_mode = "System"
        self._build_gui()

    def _build_gui(self):
        # Main container with padding
        self.main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Header
        header_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 20))
        title = ctk.CTkLabel(
            header_frame,
            text="Musalist Automation Suite",
            font=("Inter", 24, "bold")
        )
        title.pack(side="left")
        self.theme_btn = ctk.CTkSwitch(
            header_frame,
            text="Dark Mode",
            command=self.toggle_theme,
            onvalue="Dark",
            offvalue="System"
        )
        self.theme_btn.pack(side="right", padx=20)

        # Tabview with modern styling
        self.tabs = ctk.CTkTabview(
            self.main_frame,
            corner_radius=8,
            segmented_button_fg_color="#2b2b2b",
            segmented_button_selected_color="#3b8ed0",
            segmented_button_selected_hover_color="#3678b0"
        )
        self.tabs.pack(fill="both", expand=True)
        self.tabs.add("Dashboard")
        self.tabs.add("Accounts")
        self.tabs.add("Settings")
        self.tabs.add("Logs")
        self._build_dashboard()
        self._build_accounts()
        self._build_settings()
        self._build_logs()

    def _build_dashboard(self):
        dash = self.tabs.tab("Dashboard")
        dash.configure(fg_color="transparent")

        # Status Card
        status_card = ctk.CTkFrame(dash, corner_radius=12)
        status_card.pack(fill="x", padx=20, pady=(20, 10))
        ctk.CTkLabel(
            status_card,
            text="System Status",
            font=("Inter", 18, "bold")
        ).pack(anchor="w", padx=20, pady=(15, 5))
        self.status_label = ctk.CTkLabel(
            status_card,
            text="Status: Stopped",
            font=("Inter", 16),
            text_color="#e74c3c"
        )
        self.status_label.pack(anchor="w", padx=20, pady=5)
        self.last_scan_label = ctk.CTkLabel(
            status_card,
            text="Last Scan: Never",
            font=("Inter", 14)
        )
        self.last_scan_label.pack(anchor="w", padx=20, pady=(5, 15))

        # Control Buttons (Updated Colors)
        control_card = ctk.CTkFrame(dash, corner_radius=12)
        control_card.pack(fill="x", padx=20, pady=10)
        self.start_btn = ctk.CTkButton(
            control_card,
            text="Start Automation",
            fg_color="#00cc66",  # Updated brighter green
            hover_color="#00b359",  # Updated darker vibrant green
            font=("Inter", 14, "bold"),
            command=self.start_automation,
            height=40
        )
        self.start_btn.pack(side="left", padx=15, pady=15)
        self.stop_btn = ctk.CTkButton(
            control_card,
            text="Stop Automation",
            fg_color="#ff3333",  # Updated brighter red
            hover_color="#e62e2e",  # Updated darker vibrant red
            font=("Inter", 14, "bold"),
            command=self.stop_automation,
            height=40,
            state="disabled"
        )
        self.stop_btn.pack(side="left", padx=15, pady=15)

        # Statistics Card
        stats_card = ctk.CTkFrame(dash, corner_radius=12)
        stats_card.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(
            stats_card,
            text="Statistics",
            font=("Inter", 18, "bold")
        ).pack(anchor="w", padx=20, pady=(15, 5))

        stats_grid = ctk.CTkFrame(stats_card, fg_color="transparent")
        stats_grid.pack(fill="x", padx=20, pady=10)
        stats_grid.columnconfigure((0, 1), weight=1)

        # Power Listings Stats
        power_frame = ctk.CTkFrame(stats_grid, corner_radius=10)
        power_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        ctk.CTkLabel(
            power_frame,
            text="Power Listings",
            font=("Inter", 16, "bold")
        ).pack(pady=(10, 5))
        self.power_ads_detected = ctk.CTkLabel(
            power_frame,
            text="Ads Detected: 0",
            font=("Inter", 14)
        )
        self.power_ads_detected.pack(pady=5)
        self.power_ads_deleted = ctk.CTkLabel(
            power_frame,
            text="Ads Deleted: 0",
            font=("Inter", 14)
        )
        self.power_ads_deleted.pack(pady=5)
        self.power_ads_posted = ctk.CTkLabel(
            power_frame,
            text="Ads Posted: 0",
            font=("Inter", 14)
        )
        self.power_ads_posted.pack(pady=(5, 10))

        # Personal Listings Stats
        personal_frame = ctk.CTkFrame(stats_grid, corner_radius=10)
        personal_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        ctk.CTkLabel(
            personal_frame,
            text="Personal Listings",
            font=("Inter", 16, "bold")
        ).pack(pady=(10, 5))
        self.personal_ads_detected = ctk.CTkLabel(
            personal_frame,
            text="Ads Detected: 0",
            font=("Inter", 14)
        )
        self.personal_ads_detected.pack(pady=5)
        self.personal_ads_deleted = ctk.CTkLabel(
            personal_frame,
            text="Ads Deleted: 0",
            font=("Inter", 14)
        )
        self.personal_ads_deleted.pack(pady=5)
        self.personal_ads_posted = ctk.CTkLabel(
            personal_frame,
            text="Ads Posted: 0",
            font=("Inter", 14)
        )
        self.personal_ads_posted.pack(pady=(5, 10))

    def _build_accounts(self):
        acc = self.tabs.tab("Accounts")
        acc.configure(fg_color="transparent")

        card = ctk.CTkFrame(acc, corner_radius=12)
        card.pack(fill="both", expand=True, padx=20, pady=20)

        # Power Listings Account
        ctk.CTkLabel(
            card,
            text="Power Listings Account",
            font=("Inter", 16, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 5))
        self.power_email_entry = ctk.CTkEntry(card, width=400, placeholder_text="Email")
        self.power_email_entry.pack(anchor="w", padx=20, pady=5)
        self.power_email_entry.insert(0, Config.POWER_LISTINGS_EMAIL)
        self.power_password_entry = ctk.CTkEntry(card, width=400, show="*", placeholder_text="Password")
        self.power_password_entry.pack(anchor="w", padx=20, pady=5)
        self.power_password_entry.insert(0, Config.POWER_LISTINGS_PASSWORD)

        # Personal Listings Account
        ctk.CTkLabel(
            card,
            text="Personal Listings Account",
            font=("Inter", 16, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 5))
        self.personal_email_entry = ctk.CTkEntry(card, width=400, placeholder_text="Email")
        self.personal_email_entry.pack(anchor="w", padx=20, pady=5)
        self.personal_email_entry.insert(0, Config.PERSONAL_LISTINGS_EMAIL)
        self.personal_password_entry = ctk.CTkEntry(card, width=400, show="*", placeholder_text="Password")
        self.personal_password_entry.pack(anchor="w", padx=20, pady=5)
        self.personal_password_entry.insert(0, Config.PERSONAL_LISTINGS_PASSWORD)

        save_btn = ctk.CTkButton(
            card,
            text="Save Credentials",
            command=self.save_credentials,
            fg_color="#3b8ed0",
            font=("Inter", 14, "bold")
        )
        save_btn.pack(pady=20)

    def _build_settings(self):
        sett = self.tabs.tab("Settings")
        sett.configure(fg_color="transparent")

        card = ctk.CTkFrame(sett, corner_radius=12)
        card.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(
            card,
            text="Advertisement Templates",
            font=("Inter", 18, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 10))

        # Power Listings Template
        ctk.CTkLabel(
            card,
            text="Power Listings Template",
            font=("Inter", 14, "bold")
        ).pack(anchor="w", padx=20, pady=(10, 5))
        self.power_title_entry = ctk.CTkEntry(card, width=500, placeholder_text="Title")
        self.power_title_entry.pack(anchor="w", padx=20, pady=5)
        self.power_title_entry.insert(0, Config.DEFAULT_AD_TEMPLATES["power_listings"]["title"])
        self.power_content_text = ctk.CTkTextbox(card, width=500, height=80)
        self.power_content_text.pack(anchor="w", padx=20, pady=5)
        self.power_content_text.insert("0.0", Config.DEFAULT_AD_TEMPLATES["power_listings"]["content"])
        self.power_price_entry = ctk.CTkEntry(card, width=500, placeholder_text="Price Range")
        self.power_price_entry.pack(anchor="w", padx=20, pady=5)
        self.power_price_entry.insert(0, Config.DEFAULT_AD_TEMPLATES["power_listings"]["price_range"])

        # Personal Listings Template
        ctk.CTkLabel(
            card,
            text="Personal Listings Template",
            font=("Inter", 14, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 5))
        self.personal_title_entry = ctk.CTkEntry(card, width=500, placeholder_text="Title")
        self.personal_title_entry.pack(anchor="w", padx=20, pady=5)
        self.personal_title_entry.insert(0, Config.DEFAULT_AD_TEMPLATES["personal_listings"]["title"])
        self.personal_content_text = ctk.CTkTextbox(card, width=500, height=80)
        self.personal_content_text.pack(anchor="w", padx=20, pady=5)
        self.personal_content_text.insert("0.0", Config.DEFAULT_AD_TEMPLATES["personal_listings"]["content"])
        self.personal_price_entry = ctk.CTkEntry(card, width=500, placeholder_text="Price Range")
        self.personal_price_entry.pack(anchor="w", padx=20, pady=5)
        self.personal_price_entry.insert(0, Config.DEFAULT_AD_TEMPLATES["personal_listings"]["price_range"])

        save_btn = ctk.CTkButton(
            card,
            text="Save Settings",
            command=self.save_settings,
            fg_color="#3b8ed0",
            font=("Inter", 14, "bold")
        )
        save_btn.pack(pady=20)

    def _build_logs(self):
        logs = self.tabs.tab("Logs")
        logs.configure(fg_color="transparent")

        card = ctk.CTkFrame(logs, corner_radius=12)
        card.pack(fill="both", expand=True, padx=20, pady=20)

        self.log_text = ctk.CTkTextbox(
            card,
            width=800,
            height=400,
            font=("Consolas", 12),
            wrap="word"
        )
        self.log_text.pack(padx=20, pady=20, fill="both", expand=True)
        clear_btn = ctk.CTkButton(
            card,
            text="Clear Logs",
            command=self.clear_logs,
            fg_color="#f39c12",
            font=("Inter", 14, "bold")
        )
        clear_btn.pack(pady=10)

    def toggle_theme(self):
        if self.theme_mode == "System":
            ctk.set_appearance_mode("Dark")
            self.theme_mode = "Dark"
            self.theme_btn.select()
            self.theme_btn.configure(text="System Mode")
        else:
            ctk.set_appearance_mode("System")
            self.theme_mode = "System"
            self.theme_btn.deselect()
            self.theme_btn.configure(text="Dark Mode")

    def start_automation(self):
        if not self.is_running:
            self.is_running = True
            self.start_btn.configure(state="disabled")
            self.stop_btn.configure(state="normal")
            self.status_label.configure(text="Status: Running", text_color="#2ecc71")
            self.automation_thread = threading.Thread(target=self.run_automation_async)
            self.automation_thread.daemon = True
            self.automation_thread.start()
            self.log_message("Automation started")

    def stop_automation(self):
        if self.is_running:
            self.is_running = False
            self.start_btn.configure(state="normal")
            self.stop_btn.configure(state="disabled")
            self.status_label.configure(text="Status: Stopped", text_color="#e74c3c")
            self.log_message("Automation stopped")

    def run_automation_async(self):
        try:
            import asyncio
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.automation.start_automation())
        except Exception as e:
            self.log_message(f"Automation error: {e}")
            self.root.after(0, self.stop_automation)

    def save_credentials(self):
        try:
            credentials = {
                'power_email': self.power_email_entry.get(),
                'power_password': self.power_password_entry.get(),
                'personal_email': self.personal_email_entry.get(),
                'personal_password': self.personal_password_entry.get()
            }
            self.automation.credential_manager.save_credentials(credentials)
            messagebox.showinfo("Success", "Credentials saved successfully!")
            self.log_message("Credentials saved")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save credentials: {e}")
            self.log_message(f"Error saving credentials: {e}")

    def save_settings(self):
        try:
            settings = {
                'power_listings': {
                    'title': self.power_title_entry.get(),
                    'content': self.power_content_text.get("0.0", "end").strip(),
                    'price_range': self.power_price_entry.get()
                },
                'personal_listings': {
                    'title': self.personal_title_entry.get(),
                    'content': self.personal_content_text.get("0.0", "end").strip(),
                    'price_range': self.personal_price_entry.get()
                }
            }
            with open('settings.json', 'w') as f:
                json.dump(settings, f, indent=2)
            messagebox.showinfo("Success", "Settings saved successfully!")
            self.log_message("Settings saved")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save settings: {e}")
            self.log_message(f"Error saving settings: {e}")

    def clear_logs(self):
        self.log_text.delete("0.0", "end")
        self.log_message("Logs cleared")

    def log_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        self.log_text.insert("end", log_entry)
        self.log_text.see("end")

    def update_stats(self, account_type, stat_type, value):
        def do_update():
            if account_type == 'power':
                if stat_type == 'ads_detected':
                    self.power_ads_detected.configure(text=f"Ads Detected: {value}")
                elif stat_type == 'ads_deleted':
                    self.power_ads_deleted.configure(text=f"Ads Deleted: {value}")
                elif stat_type == 'ads_posted':
                    self.power_ads_posted.configure(text=f"Ads Posted: {value}")
            elif account_type == 'personal':
                if stat_type == 'ads_detected':
                    self.personal_ads_detected.configure(text=f"Ads Detected: {value}")
                elif stat_type == 'ads_deleted':
                    self.personal_ads_deleted.configure(text=f"Ads Deleted: {value}")
                elif stat_type == 'ads_posted':
                    self.personal_ads_posted.configure(text=f"Ads Posted: {value}")
        self.root.after(0, do_update)

    def run(self):
        self.root.mainloop()