const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  mode: 'development',
  entry: './webpage/index.html', // Встановіть свій власний вхідний файл
  output: {
    path: path.resolve(__dirname, 'webpage'), // Встановіть папку виводу
    filename: 'index.html', // Встановіть назву виводного файлу
  },
  plugins: [
    new CopyWebpackPlugin({
      patterns: [
        { from: './webpage/scss/helpers', to: 'css/helpers' }, 
        { from: './webpage/scss/items', to: 'css/items' },
        { from: './webpage/scss', to: 'css' },// Встановіть шляхи до вихідної та цільової папок
      ],
    }),
  ],
};
