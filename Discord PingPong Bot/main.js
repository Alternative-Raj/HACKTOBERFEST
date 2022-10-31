const { Client, GatewayIntentBits } = require('discord.js');
const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildMessages,
        GatewayIntentBits.MessageContent,
        GatewayIntentBits.GuildMembers,
    ],
});

client.on('messageCreate', message => {
    if (message.content.startsWith('ping!')) {
        message.reply('pong!');
    }
});

client.on('ready', () => {
    console.log('I am ready!');
});

client.login(process.env.BOT_TOKEN)