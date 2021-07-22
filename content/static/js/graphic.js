
function draw_chart(data){
  // set the dimensions and margins of the graph
  const margin = { top: 20, right: 30, bottom: 40, left: 90 },
  width = (0.7 * window.innerWidth) - margin.left - margin.right,
  height = 500 - margin.top - margin.bottom;

// append the svg object to the body of the page
const svg = d3.select("#graphic")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);


// Add X axis
const x = d3.scaleLinear()
  .domain([0, d3.max(data, (d) => parseInt(d["value"]))])
  .range([0, width]);
svg.append("g")
  .attr("transform", `translate(0, ${height})`)
  .call(d3.axisBottom(x))
  .selectAll("text")
  .attr("transform", "translate(-10,0)rotate(-45)")
  .style("text-anchor", "end");

// Y axis
const y = d3.scaleBand()
  .range([0, height])
  .domain(data.map(d => d.name))
  .padding(.1);
svg.append("g")
  .call(d3.axisLeft(y))

//Bars
svg.selectAll("myRect")
  .data(data)
  .join("rect")
  .attr("x", x(0))
  .attr("y", d => y(d.name))
  .attr("width", d => x(d.value))
  .attr("height", y.bandwidth())
  .attr("fill", "#146173")

}