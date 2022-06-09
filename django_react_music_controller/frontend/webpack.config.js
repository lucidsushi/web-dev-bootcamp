const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",  // entry point of the application
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: "[name].js", // name of the file that will be outputed
  },
  // show more error diffs
  // stats: {
  //   errorDetails: true,
  // },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("development"),
      },
    }),
  ],
};