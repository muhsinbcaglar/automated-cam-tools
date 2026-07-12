using System;
using System.Diagnostics;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;


namespace SIM_Watchmen_UI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            button3.Enabled = false;
            string username = Environment.UserName;
            username = username.Replace(".", "");

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            string username = Environment.UserName;
            username = username.Replace(".", "");
            string path = @"S:\CAD_Office\Muhsin\NXOPEN\Simulation_Watchmen_V1\\SIM_CONTROL_DATA\SIM_CONTROL-" + username + ".txt";
            File.WriteAllLines(path, new[] { "RUN SIMULATION" });
        }



        // PLAY
        private void button1_Click(object sender, EventArgs e)
        {
            string username = Environment.UserName;
            username = username.Replace(".", "");
            button1.Enabled = false;
            button3.Enabled = true;
            string path = @"S:\CAD_Office\Muhsin\NXOPEN\Simulation_Watchmen_V1\\SIM_CONTROL_DATA\SIM_CONTROL-" + username + ".txt";
            File.WriteAllLines(path, new[] { "RUN SIMULATION" });
            string strCmdText;
            strCmdText = "/c @py.exe S:\\\\CAD_Office\\\\Muhsin\\\\NXOPEN\\\\Simulation_Watchmen_V1\\\\SIM_Watchmen_V1.py %*";
            System.Diagnostics.Process.Start("CMD.exe", strCmdText);
        }
        // STOP
        private void button3_Click(object sender, EventArgs e)
        {
            string username = Environment.UserName;
            username = username.Replace(".", "");
            button1.Enabled = true;
            button3.Enabled = false;
            string path = @"S:\CAD_Office\Muhsin\NXOPEN\Simulation_Watchmen_V1\\SIM_CONTROL_DATA\SIM_CONTROL-" + username + ".txt";
            File.WriteAllLines(path, new[] { "STOP SIMULATION" });
        }
        // CLOSE
        private void button2_Click(object sender, EventArgs e)
        {
            string username = Environment.UserName;
            username = username.Replace(".", "");
            string path = @"S:\CAD_Office\Muhsin\NXOPEN\Simulation_Watchmen_V1\\SIM_CONTROL_DATA\SIM_CONTROL-" + username + ".txt";
            File.WriteAllLines(path, new[] { "STOP SIMULATION" });
            System.Windows.Forms.Application.Exit();

        }
    }
}
