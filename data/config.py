from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env.txt fayl ichidan quyidagilarni o'qish uchun
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
