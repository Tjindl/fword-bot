import os
import logging
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler
from content import CONTENT

# ==============================================================================
# CONFIGURATION
# ==============================================================================
# Load environment variables from .env file
load_dotenv()

# Fetch the token safely
TOKEN = os.getenv("BOT_TOKEN")

# Check if token exists (Good for debugging)
if not TOKEN:
    raise ValueError("No BOT_TOKEN found in .env file! Make sure you created it.")


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ==============================================================================
# HANDLERS
# ==============================================================================

def get_main_menu_keyboard():
    """Returns the main menu keyboard layout."""
    return [
        [
            InlineKeyboardButton("👨‍💻 Who is Tushar?", callback_data='bio'),
            InlineKeyboardButton("🛠️ The Tech Stack", callback_data='skills'),
        ],
        [
            InlineKeyboardButton("🚀 Projects", callback_data='projects'),
            InlineKeyboardButton("🔥 Why hire me?", callback_data='why'),
        ],
        [
            InlineKeyboardButton("🎲 Vibe Check", callback_data='vibe'),
            InlineKeyboardButton("📬 Contact Me", callback_data='contact'),
        ]
    ]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends the welcome menu when the user types /start"""
    
    reply_markup = InlineKeyboardMarkup(get_main_menu_keyboard())
    
    await update.message.reply_text(
        "**Hello.** 👋\n\n"
        "I am Tushar's automated assistant.\n"
        "You asked for real, so here is the real info without the fluff.\n\n"
        "Select an option to inspect my code and character:",
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles button clicks"""
    query = update.callback_query
    
    # Must answer the query to stop the loading animation on the button
    await query.answer()
    
    # --- NAVIGATION ---
    if query.data == 'main_menu':
        await query.edit_message_text(
            text="**Main Menu**\nSelect an option below:",
            reply_markup=InlineKeyboardMarkup(get_main_menu_keyboard()),
            parse_mode=ParseMode.MARKDOWN
        )
        return

    # --- CONTENT LOGIC ---
    response_text = CONTENT.get(query.data, "Content not found.")
    
    # Create a "Back" button to return to the main menu
    back_button = [[InlineKeyboardButton("🔙 Back to Main Menu", callback_data='main_menu')]]
    reply_markup = InlineKeyboardMarkup(back_button)

    # Edit the text to show the content requested
    await query.edit_message_text(
        text=response_text,
        reply_markup=reply_markup,
        parse_mode=ParseMode.MARKDOWN
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Log the error and send a telegram message to notify the developer."""
    logging.error(msg="Exception while handling an update:", exc_info=context.error)

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == '__main__':
    # Build the application
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    # Add error handler
    application.add_error_handler(error_handler)
    
    print("Bot is polling... (Press Ctrl+C to stop)")
    
    # Run the bot
    application.run_polling()