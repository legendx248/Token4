TOKEN = os.environ.get('DISCORD_TOKEN')

if not TOKEN:

raise SystemExit("DISCORD_TOKEN not set")

bot.run(TOKEN)
