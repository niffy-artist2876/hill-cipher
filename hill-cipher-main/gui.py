import tkinter as tk
from tkinter import ttk, messagebox

from cipher import encrypt, decrypt

FIXED_KEY = [[3, 3], [2, 5]]


class HillCipherGUI:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Hill Cipher")
        self.root.geometry("700x470")
        self.root.minsize(680, 440)

        self.colors = {
            "bg": "#eef3ff",
            "card": "#ffffff",
            "primary": "#2f6df6",
            "primary_dark": "#1f55cc",
            "accent": "#00a88f",
            "text": "#1d2a45",
            "muted": "#5e6b85",
        }

        self.message_var = tk.StringVar()
        self.encrypted_var = tk.StringVar()
        self.decrypted_var = tk.StringVar()

        self._configure_styles()
        self._build_ui()

    def _configure_styles(self) -> None:
        # Centralized ttk styling so we can keep a consistent colorful theme.
        self.root.configure(bg=self.colors["bg"])
        style = ttk.Style(self.root)
        if "clam" in style.theme_names():
            style.theme_use("clam")

        style.configure("App.TFrame", background=self.colors["bg"])
        style.configure(
            "Card.TLabelframe",
            background=self.colors["card"],
            bordercolor=self.colors["primary"],
            borderwidth=2,
            relief="solid",
        )
        style.configure(
            "Card.TLabelframe.Label",
            background=self.colors["card"],
            foreground=self.colors["primary"],
            font=("Segoe UI", 10, "bold"),
        )
        style.configure(
            "Title.TLabel",
            background=self.colors["bg"],
            foreground=self.colors["text"],
            font=("Segoe UI", 20, "bold"),
        )
        style.configure(
            "Subtle.TLabel",
            background=self.colors["bg"],
            foreground=self.colors["muted"],
            font=("Segoe UI", 10),
        )
        style.configure(
            "Text.TLabel",
            background=self.colors["card"],
            foreground=self.colors["text"],
            font=("Segoe UI", 10),
        )
        style.configure(
            "Input.TEntry",
            fieldbackground="#ffffff",
            foreground=self.colors["text"],
            insertcolor=self.colors["text"],
            padding=6,
        )
        style.configure(
            "Output.TEntry",
            fieldbackground="#f1f6ff",
            foreground=self.colors["text"],
            padding=6,
        )
        style.map("Output.TEntry", fieldbackground=[("readonly", "#f1f6ff")])
        style.configure(
            "Accent.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(14, 8),
            foreground="#ffffff",
            background=self.colors["primary"],
            borderwidth=0,
        )
        style.map(
            "Accent.TButton",
            background=[("active", self.colors["primary_dark"])],
            foreground=[("active", "#ffffff")],
        )
        style.configure(
            "Ghost.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(14, 8),
            foreground="#ffffff",
            background=self.colors["accent"],
            borderwidth=0,
        )
        style.map(
            "Ghost.TButton",
            background=[("active", "#008f79")],
            foreground=[("active", "#ffffff")],
        )

    def _build_ui(self) -> None:
        container = ttk.Frame(self.root, padding=20, style="App.TFrame")
        container.pack(fill="both", expand=True)

        color_bar = tk.Frame(container, bg=self.colors["primary"], height=6)
        color_bar.pack(fill="x", pady=(0, 12))

        ttk.Label(
            container,
            text="Hill Cipher",
            style="Title.TLabel",
        ).pack(anchor="w")
        ttk.Label(
            container,
            text="Encrypt and decrypt text using a 2x2 key matrix",
            style="Subtle.TLabel",
        ).pack(anchor="w", pady=(3, 14))

        msg_frame = ttk.LabelFrame(
            container, text="Input Message", padding=12, style="Card.TLabelframe"
        )
        msg_frame.pack(fill="x")

        msg_entry = ttk.Entry(msg_frame, textvariable=self.message_var, style="Input.TEntry")
        msg_entry.pack(fill="x")
        msg_entry.focus_set()

        key_frame = ttk.LabelFrame(container, text="Key", padding=12, style="Card.TLabelframe")
        key_frame.pack(fill="x", pady=12)
        # Key is intentionally fixed to match the original CLI behavior.
        ttk.Label(
            key_frame,
            text="Using fixed key matrix: [[3, 3], [2, 5]]",
            style="Text.TLabel",
        ).pack(anchor="w")

        btn_frame = ttk.Frame(container, style="App.TFrame")
        btn_frame.pack(fill="x", pady=(0, 12))

        ttk.Button(
            btn_frame,
            text="Encrypt + Decrypt",
            command=self.run_cipher_flow,
            style="Accent.TButton",
        ).pack(side="left", padx=(0, 8))

        ttk.Button(
            btn_frame,
            text="Clear",
            command=self.clear_outputs,
            style="Ghost.TButton",
        ).pack(side="left")

        output_frame = ttk.LabelFrame(
            container, text="Output", padding=12, style="Card.TLabelframe"
        )
        output_frame.pack(fill="both", expand=True)

        ttk.Label(output_frame, text="Encrypted", style="Text.TLabel").pack(anchor="w")
        ttk.Entry(
            output_frame,
            textvariable=self.encrypted_var,
            state="readonly",
            style="Output.TEntry",
        ).pack(
            fill="x", pady=(2, 10)
        )

        ttk.Label(output_frame, text="Decrypted", style="Text.TLabel").pack(anchor="w")
        ttk.Entry(
            output_frame,
            textvariable=self.decrypted_var,
            state="readonly",
            style="Output.TEntry",
        ).pack(
            fill="x", pady=(2, 0)
        )

    def run_cipher_flow(self) -> None:
        msg = self.message_var.get()
        if not msg.strip():
            messagebox.showerror("Missing Input", "Please enter a message.")
            return

        try:
            # Keep the core behavior: encrypt input first, then decrypt encrypted text.
            encrypted = encrypt(msg, FIXED_KEY)
            decrypted = decrypt(encrypted, FIXED_KEY)
            # pad() can append one trailing A for this 2x2 setup; hide that in UI output.
            if decrypted.endswith("A"):
                decrypted = decrypted[:-1]
        except Exception as exc:
            messagebox.showerror("Error", str(exc))
            return

        self.encrypted_var.set(encrypted)
        self.decrypted_var.set(decrypted)

    def clear_outputs(self) -> None:
        self.encrypted_var.set("")
        self.decrypted_var.set("")


def main() -> None:
    root = tk.Tk()
    app = HillCipherGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
