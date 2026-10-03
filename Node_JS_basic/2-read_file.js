const fs = require('fs');

function countStudents(path) {
  let content;

  try {
    content = fs.readFileSync(path, 'utf-8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }

  const lines = content.split('\n').filter((line) => line.trim() !== '');

  if (lines.length <= 1) {
    console.log('Number of students: 0');
    return;
  }

  const students = lines.slice(1);
  console.log(`Number of students: ${students.length}`);

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

  for (const [field, names] of Object.entries(fields)) {
    console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
  }
}

module.exports = countStudents;
