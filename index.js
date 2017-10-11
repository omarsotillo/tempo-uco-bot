/**
 * (c) Omar Sotillo Franco <omarsotillofranco@gmail.com>
 */
const logic = require('./schedule/logic');
const { Composer, Extra, Markup } = require('micro-bot');

// Creation of the bot
const bot = new Composer();

// Keyboard markups templates
const baseKeyboard = Markup
  .keyboard([
    ['🚌 Autobuses'],
    ['🚋 Trenes'],
    ['📢 Disponibilidad', '💰 Precios', '👥 Contacto'],
  ])
  .resize()
  .extra();

const pricesKeyboard = Markup.inlineKeyboard([
  Markup.callbackButton('Precios del autobus', 'busPrices'),
  Markup.callbackButton('Precios de trenes', 'trainPrices'),
]).extra();

const busesKeyboard = Markup.inlineKeyboard([
  Markup.callbackButton('🚌🏘 Bus Colón️', 'busColon'),
  Markup.callbackButton('🚌🏫 Bus Rabanales', 'busRabanales'),
]).extra();

const trainsKeyboard = Markup.inlineKeyboard([
  Markup.callbackButton('🚋🏘 Tren Renfe️', 'trenRenfe'),
  Markup.callbackButton('🚋🏫 Tren Rabanales', 'trenRabanales'),
]).extra();

// start command
bot.command('/start', ({ replyWithMarkdown }) => replyWithMarkdown(`
*Buenas! Soy un bot hehe ^^*
Te otorgo información sobre _Servicios de Transporte del Campus Rabanales._

Hago lo siguiente:
  🚌 Autobuses : Salidas desde Rabanales y Colón.
  🚉 Trenes : Salidas desde Rabanales y Renfe.
  🕑 Horarios Completos: Foto con horarios completos.
  📅 Disponibilidad : Información sobre servicios.
  💡 Contacto: ¿Quién me ha hecho? Háblale
`, baseKeyboard));

// 1st level keyboards
bot.hears('🚌 Autobuses', ({ reply }) => reply('Próximas salidas de autobuses 🚌 ', busesKeyboard));
bot.hears('🚋 Trenes', ({ reply }) => reply('Próximas salidas de trenes 🚋', trainsKeyboard));
bot.hears('📢 Disponibilidad', ({ reply }) => reply('* ✅ Actualmente el servicio funciona sin incidencias*', Extra.markdown()));
bot.hears('💰 Precios', ({ reply }) => reply('Información de precios', pricesKeyboard));
bot.hears('👥 Contacto', ({ reply }) => reply('Este bot fue creado por *Omar Sotillo Franco* @omar\\_sotillo. \n Si tienes alguna sugerencia o problema contacta con él.', Extra.markdown()));

// Keyboards actions
// Bus and trains actions
bot.action('busColon', ({ reply }) => reply(`El siguiente autobús sale de _Colón_ a las : *${logic.comingBusColon()}*`, Extra.markdown()));
bot.action('busRabanales', ({ reply }) => reply(`El siguiente autobús sale de _Rabanales_ a las : *${logic.comingBusRabanales()}*`, Extra.markdown()));
bot.action('trenRenfe', ({ reply }) => reply(`El siguiente tren sale de _Renfe_ a las :  *${logic.comingTrainRenfe()}*`, Extra.markdown()));
bot.action('trenRabanales', ({ reply }) => reply(`El siguiente tren sale de _Rabanales_ a las : *${logic.comingTrainRabanales()}*`, Extra.markdown()));

// Prices
bot.action('busPrices', ({ reply }) => reply(
  `
*BONOBÚS*
  Tarjeta Bonobús: *0,72€* (Cada viaje)
  Tarjeta Bonobús Estudiante: *0,58€* (Cada viaje)
  Tarjeta Bonobús Familia: *0,64€* (Cada viaje)
*ABONOS*
  Tarjeta abono 30 días: *33,00€* 
  Tarjeta abono 30 días (con descuento) : *28,00€* 
  Billete sencillo : *1,30 €*
  `,
  // eslint-disable-next-line comma-dangle
  Extra.markdown()
));
bot.action('trainPrices', ({ reply }) => reply(
  `
*Billetes sencillos*
  Ida: *1,90€*
  ida y vuelta: *3,00€* 
*ABONOS*
  Bono 10: *12,70€* 
  Bono mensual: *30,30€* 
  Abono semestral: *121,45 €*
  `,
  // eslint-disable-next-line comma-dangle
  Extra.markdown()
));


// First level actions
module.exports = bot;
