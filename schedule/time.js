module.exports = {
  getTime() {
    const d = new Date();
    let dateMinutes = d.getMinutes();
    let dateHours = d.getHours();
    // Adding zero function
    if (dateMinutes < 10) {
      dateMinutes = `0${dateMinutes}`;
    }
    if (dateHours < 10) {
      dateHours = `0${dateHours}`;
    }
    console.log(`${d.getHours()}:${dateMinutes}`);
    return `${dateHours}:${dateMinutes}`;
  },
};
