\documentclass{article}
\usepackage{listings}
\usepackage{hyperref}
\usepackage{geometry}
\geometry{margin=1in}
\title{Beef Supply Chain Cybersecurity Framework}
\author{}
\date{}

\begin{document}

\maketitle

\section*{Project Overview}

This project presents a simulation-driven cybersecurity framework for modeling failures in the beef supply chain. It includes:

\begin{enumerate}
    \item A multi-system failure simulation (farm to processing to logistics)
    \item AI-based anomaly detection to catch early signs of attack or malfunction
    \item A planned blockchain traceability layer using Ethereum smart contracts
\end{enumerate}

\section*{Repository Structure}

\begin{lstlisting}
.
├── cyber_beef_sim.py                Main cascading failure simulation
├── system_config.json               System dependencies and parameters
├── visualize_failures.py            Gantt chart visualization of failures
├── ai_anomaly_sim.py                AI anomaly detection simulator (basic)
├── ai_anomaly_log.csv               Output from AI simulation
├── anomaly_heatmap_animator.py     Animated health status visualization
├── ai_anomaly_log_realistic.csv     Realistic anomaly log with evaluation labels
├── blockchain_logger.py            Smart contract interface (planned)
├── BeefTrace.sol                    Solidity contract for traceability (planned)
└── README.md                        Project documentation
\end{lstlisting}

\section*{1. Cascading Failure Simulation}

The file \texttt{cyber_beef_sim.py} uses SimPy to simulate cascading cyber failures across interconnected systems in the beef supply chain.

\textbf{How it works:}

\begin{itemize}
    \item Each system can fail due to random events or dependencies
    \item Recovery times are also randomized
    \item Logs are saved in the format \texttt{failure\_logs\_YYYYMMDD\_HHMM.csv}
\end{itemize}

\textbf{Run:}
\begin{lstlisting}[language=bash]
python cyber_beef_sim.py
\end{lstlisting}

\textbf{Visualize:}
\begin{lstlisting}[language=bash]
python visualize_failures.py
\end{lstlisting}

Generates \texttt{failure\_timeline.png}, a Gantt chart of system states.

\section*{2. AI Anomaly Detection Layer}

This component simulates AI-based detection of abnormal system behavior.

\subsection*{Basic Simulation}

\texttt{ai\_anomaly\_sim.py} generates synthetic data showing:
\begin{itemize}
    \item Time-series sensor fluctuations
    \item Detected anomalies
    \item Labeled anomaly log
\end{itemize}

\textbf{Run:}
\begin{lstlisting}[language=bash]
python ai_anomaly_sim.py
\end{lstlisting}

Outputs:
\begin{itemize}
    \item \texttt{ai\_anomaly\_log.csv}
    \item \texttt{ai\_anomaly\_plot.png}
\end{itemize}

\subsection*{Realistic Anomaly Modeling}

A planned script \texttt{generate\_ai\_anomaly\_log.py} will:

\begin{itemize}
    \item Reduce anomaly frequency
    \item Add detection noise (false positives and false negatives)
    \item Label output with TP, FP, TN, FN for evaluation
\end{itemize}

\section*{Animated Visualization}

\texttt{anomaly\_heatmap\_animator.py} animates a grid of systems:
\begin{itemize}
    \item Green = normal state
    \item Red = anomaly detected
\end{itemize}

\textbf{Run:}
\begin{lstlisting}[language=bash]
python anomaly_heatmap_animator.py
\end{lstlisting}

Output: \texttt{ai\_anomaly\_heatmap.gif}

\section*{3. Blockchain Traceability Layer (Planned)}

To ensure traceable, tamper-proof event logs, the system will interface with a blockchain.

\begin{itemize}
    \item \texttt{BeefTrace.sol} defines a smart contract to log critical events
    \item \texttt{blockchain\_logger.py} connects the simulation to the contract using Web3.py
\end{itemize}

Integration with the main simulation is under development.

\section*{End-to-End Flow}

\begin{enumerate}
    \item Run the cascading failure simulation
    \item Use AI simulation to detect anomalies
    \item Visualize failures and anomaly heatmaps
    \item Log important security events to blockchain (planned)
\end{enumerate}

\section*{Requirements}

\begin{lstlisting}[language=bash]
pip install simpy pandas matplotlib web3
\end{lstlisting}

For blockchain:
\begin{itemize}
    \item Ganache for local Ethereum node
    \item Remix IDE to compile and deploy \texttt{BeefTrace.sol}
\end{itemize}

\section*{Future Work}

\begin{itemize}
    \item Integrate AI anomaly detection directly into \texttt{cyber\_beef\_sim.py}
    \item Finalize blockchain contract deployment and logging
    \item Build an interactive dashboard using Dash or Plotly
\end{itemize}

\section*{License}

MIT License
\end{document}

