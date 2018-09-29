var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.render('index', { matrix: mockData });
});

const euro1 = "The European languages are members of the same family."
const euro2 = "Their separate existence is a myth. \
  For science, music, sport, etc, Europe uses the same vocabulary."
const euro3 = "The languages only differ in their grammar, \
  their pronunciation and their most common words."

const kafka1 = "One morning, when Gregor Samsa woke from troubled dreams, \
  he found himself transformed in his bed into a horrible vermin."
const kafka2 = "He lay on his armour-like back, \
  and if he lifted his head a little he could see his brown belly, \
  slightly domed and divided by arches into stiff sections."
const kafka3 = "The bedding was hardly able to cover it and \
  seemed ready to slide off any moment."

const mockData = [
  [
    { title: "Li Europan lingues 1", description: euro1 },
    { title: "Li Europan lingues 2", description: euro2 },
    { title: "Li Europan lingues 3", description: euro3 }
  ],
  [
    { title: "kafka 1", description: kafka1 },
    { title: "kafka 2", description: kafka2 },
    { title: "kafka 3", description: kafka3 }
  ]
];

module.exports = router;
