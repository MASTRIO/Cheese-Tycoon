import javax.swing.*;
import java.awt.*;
import javax.swing.JOptionPane;

class gui {
    public static void main(String args[]) {

        // Make the frame thing
        JFrame frame = new JFrame("Just Another Game About Cheese");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 600);

        // MANu Bar
        JMenuBar mb = new JMenuBar();
        JMenu m1 = new JMenu("File");
        JMenu m2 = new JMenu("Help");
        mb.add(m1);
        mb.add(m2);
        JMenuItem m11 = new JMenuItem("New Game");
        JMenuItem m12 = new JMenuItem("Open Game");
        JMenuItem m13 = new JMenuItem("Save Game");
        m1.add(m11);
        m1.add(m12);
        m1.add(m13);
        JMenuItem m21 = new JMenuItem("Tutorial");
        JMenuItem m22 = new JMenuItem("Wiki");
        JMenuItem m23 = new JMenuItem("Report Bug");
        m2.add(m21);
        m2.add(m22);
        m2.add(m23);

        // Creating the panel at bottom and adding components
        JPanel panel = new JPanel();
        JTextField commandInput = new JTextField(20);
        JButton runCommand = new JButton("Run Command");
        panel.add(commandInput);
        panel.add(runCommand);

        // Text Area at the Center
        JTextArea ta = new JTextArea();

        //Adding Components to the frame.
        frame.getContentPane().add(BorderLayout.SOUTH, panel);
        frame.getContentPane().add(BorderLayout.NORTH, mb);
        frame.getContentPane().add(BorderLayout.CENTER, ta);
        frame.setVisible(true);
    }
}