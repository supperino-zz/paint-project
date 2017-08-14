import java.awt.Canvas;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.awt.image.BufferStrategy;

import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class RenderThread extends JFrame implements Runnable{
    
    private FrameRate framerate;
    private volatile boolean running;
    private Thread gameThread;
    private BufferStrategy bs;
    
    public RenderThread() {
        framerate = new FrameRate();
    }
    
    public void run() {
        running = true;
        framerate.initialize();
        while(running) {
            gameLoop();
        }
    }
    /*
     * Enquanto a off-screen image (contentsLost) do bufferStrategy puder ser desenhada
     * Ele cria um novo graphics( getDrawGraphics)
     * Desenha nesse novo graphics
     * E deleta o atual graphics mostrado
     * bs.show faz o efeito de dublebuffering, trocando o graphics printado, pelo o que esta na offscreen
     * 
     * */
    private void gameLoop() {
        do {
            do {
                Graphics g = null;
                try {
                    g = bs.getDrawGraphics();
                    g.clearRect(0, 0, getWidth(), getHeight());
                    render(g);
                } finally {
                    if(g!=null) {
                        g.dispose();
                    }
                }
            } while(bs.contentsRestored());
            bs.show();
        }while(bs.contentsLost());
        
    }

    private void render(Graphics g) {
        // TODO Auto-generated method stub
        framerate.calculate();
        g.setColor(Color.GREEN);
        g.drawString(framerate.getFrameRate(), 30, 30);
        
    }

    protected void createAndShowGUI() {
        Canvas canvas = new Canvas();
        canvas.setSize(320 , 240);
        canvas.setBackground(Color.black);
        canvas.setIgnoreRepaint(true);
        getContentPane().add(canvas);
        setTitle("Rendering Thread");
        setIgnoreRepaint(true);
        pack();
        
        setVisible(true);
        canvas.createBufferStrategy(2);
        bs = canvas.getBufferStrategy();
        
        gameThread = new Thread(this);
        gameThread.start();
    }
    
    protected void onWindowClosing() {
        try {
            running = false;
            gameThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.exit(0);
    }
    
    public static void main(String[] args) {
        final RenderThread renderthread = new RenderThread();
        
        renderthread.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                renderthread.onWindowClosing();
            }
        });
        
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                renderthread.createAndShowGUI();
            }
        });
    }
    
}
