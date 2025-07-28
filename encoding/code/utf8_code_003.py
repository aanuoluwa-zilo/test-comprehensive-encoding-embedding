# UTF-8 encoded file 3
# Special characters: éñáüß
# Emoji: 🚀🎉🌟
class UTF8Processor3:
    def __init__(self):
        self.special_chars = "éñáüß"
        self.emoji = "🚀🎉🌟"
    
    def process_utf8(self, text):
        return text.encode('utf-8').decode('utf-8')
