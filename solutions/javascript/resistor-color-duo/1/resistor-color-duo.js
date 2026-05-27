const COLORS=[
  "black",
  "brown",
  "red",
  "orange",
  "yellow",
  "green",
  "blue",
  "violet",
  "grey",
  "white"
];
export const decodedValue=(colors)=>{
  const first=COLORS.indexOf(colors[0]);
  const second=COLORS.indexOf(colors[1]);
  return Number(`${first}${second}`);
};