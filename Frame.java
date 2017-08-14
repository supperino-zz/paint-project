/*import java.awt.Color;
import java.awt.Dimension;

import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class Frame extends JFrame{
    private FrameRate frameRate;
    
    public Frame() {
        frameRate = new FrameRate();
    }
    
    protected void createAndShowGui() {
        GamePanel gamePanel = new GamePanel(frameRate);
        gamePanel.setBackground(Color.BLACK);
        gamePanel.setPreferredSize(new Dimension(320,240));
        getContentPane().add( gamePanel );
        setDefaultCloseOperation( EXIT_ON_CLOSE );
        setTitle( "Hello World!" );
        pack();
        frameRate.initialize();
        setVisible( true );
    }
    
    public static void main (String[] args) {
        final Frame frame = new Frame();
        SwingUtilities.invokeLater( new Runnable() {
            public void run() {
            frame.createAndShowGui();
            }
            });
    }

}
*/