/**
 * (c) Omar Sotillo Franco <omarsotillofranco@gmail.com>
 */

const { Composer, Markup, Extra } = require('micro-bot')

// Creation of the bot
const bot = new Composer()

// start command
bot.command('/start', (ctx) => ctx.reply('_Welcome!_', Extra.markdown()))

bot.command('/trenes', (ctx) => {
  return ctx.reply('<b>Coke</b> or <i>Pepsi?</i>', Extra.HTML().markup((m) =>
    m.inlineKeyboard([
      m.callbackButton('Trenes', '/tren'),
      m.callbackButton('Autobuses', 'Autobuses')
    ])))
})

bot.command('/tren', (ctx) => {
  return ctx.reply('<b>Coke</b> or <i>Pepsi?</i>', Extra.HTML().markup((m) =>
    m.inlineKeyboard([
      m.callbackButton('Salida Estación', '/bus'),
      m.callbackButton('Salida Rabanales', '/trenRabanales')
    ])))
})

bot.command('/bus', (ctx) => {
  return ctx.reply('<b>Coke</b> or <i>Pepsi?</i>', Extra.HTML().markup((m) =>
    m.inlineKeyboard([
      m.callbackButton('Salida Colón', '/busColon'),
      m.callbackButton('Salida Campus Rabanales', '/busRabanales')
    ])))
})

module.exports = bot
