const busModule = require('./bus_schedule');
const trainModule = require('./train_schedule');
const time = require('./time');

module.exports = {
  // BUS
  upcomingBusRabanales() {
    let nextArrival = 'El siguiente bus sale mañana.';
    const BreakException = {};
    try {
      busModule.rabanalesBus.some((comingBus) => {
        if (comingBus > time.getTime()) {
          nextArrival = comingBus;
          throw BreakException;
        }
      });
    } catch (e) {
      if (e !== BreakException) throw e;
    }
    return nextArrival;
  },
  upcomingBusColon() {
    let nextArrival = 'El siguiente bus sale mañana.';
    const BreakException = {};
    try {
      busModule.colonBus.some((comingBus) => {
        if (comingBus > time.getTime()) {
          nextArrival = comingBus;
          throw BreakException;
        }
      });
    } catch (e) {
      if (e !== BreakException) throw e;
    }
    return nextArrival;
  },
};
