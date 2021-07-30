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


const x = d3.scaleLinear()
  .range([0, width])
  

const xAxis = svg.append("g")
  .attr("transform", `translate(0, ${height})`) // colocar o eixo X na parte de baixo


const y = d3.scaleBand()
  .range([0, height])
  .padding(.1);

const yAxis = svg.append("g")

// ------------------------------------
function draw_chart(data, max_domain=350) {

  x.domain([0, max_domain])

  xAxis.call(d3.axisBottom(x))
    .selectAll("text")
    .attr("transform", "translate(-10,0)rotate(-45)")
    .style("text-anchor", "end");

  // Y axis
  y.domain(data.map(d => d.name))
  yAxis.call(d3.axisLeft(y))

  //Bars
  const u = svg.selectAll("rect")
    .data(data)


  u.enter()
    .append("rect")
    .merge(u)
    
    .transition()
    .attr("y", d => y(d.name))
    .attr("height", y.bandwidth())
    .attr("fill", "#146173")
    
    .transition()
    .duration(600)
    .ease(d3.easeCubicIn)
    .attr("x", x(0))
    .attr("width", d => x(d.value))


}