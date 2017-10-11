/* eslint-disable array-callback-return */

const busModule = require('./bus_schedule');
const trainModule = require('./train_schedule');
const time = require('./time');

module.exports = {
  // BUS
  comingBusRabanales() {
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
  comingBusColon() {
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
  comingTrainRabanales() {
    let nextArrival = 'El sig.';
    const BreakException = {};
    try {
      trainModule.rabanalesTrain.some((comingBus) => {
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
  comingTrainRenfe() {
    let nextArrival = 'El sig.';
    const BreakException = {};
    try {
      trainModule.renfeTrain.some((comingBus) => {
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
