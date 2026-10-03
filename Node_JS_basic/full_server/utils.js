import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');

    if (lines.length <= 1) {
      resolve({});
      return;
    }

    const students = lines.slice(1);
    const fields = {};

    for (const student of students) {
      const record = student.split(',');
      if (record.length >= 4) {
        const firstname = record[0].trim();
        const field = record[3].trim();

        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    }

    resolve(fields);
  });
});

export default readDatabase;
