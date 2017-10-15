module.exports = {
  getTime() {
    const d = new Date();
    let dateMinutes = d.getMinutes();
    // Adding zero function
    if (dateMinutes < 10) {
      dateMinutes = `0${dateMinutes}`;
    }
    console.log(`${d.getHours()}:${dateMinutes}`);
    return `${d.getHours()}:${dateMinutes}`;
  },
};
