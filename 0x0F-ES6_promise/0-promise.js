export default function getResponseFromAPI() {
    return new Promise((resolve, reject) => {
      if (true) {
        resolve('hey');
      } else {
        reject(new Error('error'));
      }
    });
  }
