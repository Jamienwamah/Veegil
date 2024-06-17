import React, { useState, useEffect, useCallback } from "react";
import { Bar } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const BarChart = () => {
  const [chartData, setChartData] = useState({
    labels: ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"],
    datasets: [
      {
        label: "Sales $",
        data: [18127, 22201, 19490, 17938, 24182, 17842, 22475],
        borderColor: "rgb(53, 162, 235)",
        backgroundColor: "rgb(53, 162, 235, 0.4)",
      },
    ],
  });

  const [chartOptions, setChartOptions] = useState({
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Daily Revenue",
      },
    },
    maintainAspectRatio: false,
    responsive: true,
  });

  // Let's define handleNewTransaction inside a useCallback hook
  const handleNewTransaction = useCallback(() => {
    // Then we proceed to generate random transaction amount
    const newTransactionAmount = Math.floor(Math.random() * 10000);
    const newChartData = { ...chartData };
    newChartData.datasets[0].data.push(newTransactionAmount);
    setChartData(newChartData);
  }, [chartData]);

  // We need to simulate new transaction every 5 seconds
  useEffect(() => {
    const intervalId = setInterval(handleNewTransaction, 5000);
    return () => clearInterval(intervalId);
  }, [handleNewTransaction]); // Let's include handleNewTransaction in the dependency array

  return (
    <>
      <div className="w-full md:col-span-2 relative lg:h-[70vh] h-[50vh] m-auto p-4 border rounded-lg bg-white">
        <Bar data={chartData} options={chartOptions} />
      </div>
    </>
  );
};

export default BarChart;
