import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';

interface WelcomeProps {
  disabled: boolean;
  startButtonText: string;
  onStartCall: () => void;
}

export const Welcome = ({
  disabled,
  startButtonText,
  onStartCall,
  ref,
}: React.ComponentProps<'div'> & WelcomeProps) => {
  return (
    <section
      ref={ref}
      inert={disabled}
      className={cn(
        'bg-background fixed inset-0 mx-auto flex min-h-screen flex-col items-center justify-center p-4 overflow-hidden',
        'text-center gap-4',
        disabled ? 'z-10' : 'z-20'
      )}
    >
            <div className="relative inline-block max-h-screen flex flex-col items-center justify-center px-4">
        {/* GIF */}
        <img
          src="/SIFRA.gif"
          alt="SIFRA"
          className="w-full max-w-[800px] h-auto object-contain"
        />

        {/* Overlay content */}
        <div className="mt-8 text-center">
          <Button
            variant="primary"
            size="lg"
            onClick={() => {
              // Play button click sound
              const clickSound = new Audio("/button-click.m4a");
              clickSound.volume = 0.3;
              clickSound.play();

              // Call your original function
              onStartCall();
            }}
            className={cn(
              "px-6 py-4 sm:px-8 sm:py-6",
              "text-lg sm:text-xl font-bold",
              "bg-cyan-500/90 hover:bg-cyan-400/90",
              "shadow-[0_0_30px_rgba(0,255,255,0.3)]",
              "hover:shadow-[0_0_50px_rgba(0,255,255,0.5)]",
              "backdrop-blur-sm",
              "rounded-2xl",
              "border-2 border-cyan-400/50",
              "transition-all duration-300",
              "animate-pulse hover:animate-none",
              "font-mono tracking-wide",
              "max-w-[90vw]"
            )}
          >
            {startButtonText}
          </Button>
        </div>
      </div>
      <footer className="fixed bottom-5 left-0 z-20 flex w-full items-center justify-center">
        <p className="text-fg1 max-w-prose pt-1 text-xs leading-5 font-normal text-pretty md:text-sm">
          Developed by {' '}
          <a
            target="_blank"
            rel="noopener noreferrer"
            href="https://www.instagram.com/buildwith_hamid/"
            className="underline"
          >
            Hamid kamal
          </a>
          .
        </p>
      </footer>
    </section>
  );
};
