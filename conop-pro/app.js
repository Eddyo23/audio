const express = require('express');
const bodyParser = require('body-parser');
const PDFDocument = require('pdfkit');
const fs = require('fs');
const path = require('path');

const app = express();

app.use(express.static('public'));
app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  res.render('form');
});

app.post('/generate', (req, res) => {
  const data = req.body;

  let doc;
  if (data.aspectRatio === '16:9') {
    doc = new PDFDocument({ size: [1280, 720] });
  } else {
    doc = new PDFDocument({ size: [960, 720] });
  }

  const filename = `output/CONOP_${Date.now()}.pdf`;
  const filepath = path.join(__dirname, filename);
  const writeStream = fs.createWriteStream(filepath);
  doc.pipe(writeStream);

  doc.fontSize(20).text('CONOP Document', { align: 'center' }).moveDown(1.5);

  Object.entries(data).forEach(([key, value]) => {
    if (key !== 'aspectRatio') {
      doc.fontSize(12).text(`${key}: ${Array.isArray(value) ? value.join(', ') : value}`);
      doc.moveDown(0.5);
    }
  });

  doc.end();

  writeStream.on('finish', () => {
    res.download(filepath, 'CONOP.pdf', () => {
      fs.unlink(filepath, () => {});
    });
  });

  writeStream.on('error', (err) => {
    console.error('PDF write error:', err);
    res.status(500).send('Error generating PDF');
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));