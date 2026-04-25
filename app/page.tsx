"use client";

import { useState } from "react";
import { CryptarithmeticCSP, Mapping, SolutionDetails } from "@/lib/csp_solver";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Badge } from "@/components/ui/badge";
import { ArrowRight, Calculator, CheckCircle2, AlertCircle, Play, ChevronRight, Sparkles } from "lucide-react";

export default function Home() {
  const [equation, setEquation] = useState("SEND + MORE = MONEY");
  const [solutions, setSolutions] = useState<{ mapping: Mapping; details: SolutionDetails }[] | null>(null);
  const [isSolving, setIsSolving] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [solveTime, setSolveTime] = useState<number>(0);

  const EXAMPLES = [
    "SEND + MORE = MONEY",
    "CROSS + ROADS = DANGER",
    "TWO * TWO = THREE",
    "BASE + BALL = GAMES"
  ];

  const handleSolve = () => {
    setIsSolving(true);
    setError(null);
    setSolutions(null);
    setSolveTime(0);

    // Use setTimeout to allow UI to breathe and show "Solving" state
    setTimeout(() => {
      try {
        const start = performance.now();
        const solver = new CryptarithmeticCSP(equation);
        const rawSolutions = solver.solve();
        const fullSolutions = rawSolutions.map((sol) => ({
          mapping: sol,
          details: solver.getSolutionDetails(sol),
        }));
        
        const end = performance.now();
        setSolveTime(Math.round(end - start));
        setSolutions(fullSolutions);
      } catch (err: any) {
        setError(err.message || "Failed to parse or solve equation.");
      } finally {
        setIsSolving(false);
      }
    }, 50);
  };

  return (
    <main className="min-h-screen py-12 px-4 sm:px-6 lg:px-8 relative overflow-hidden flex flex-col items-center">
      {/* Aesthetic Background Orbs */}
      <div className="absolute top-[-10%] left-[-10%] w-96 h-96 bg-primary/20 blur-[120px] rounded-full pointer-events-none" />
      <div className="absolute bottom-[-10%] right-[-10%] w-96 h-96 bg-purple-600/20 blur-[120px] rounded-full pointer-events-none" />

      <div className="w-full max-w-4xl z-10 space-y-8 animate-in fade-in slide-in-from-bottom-8 duration-1000">
        <div className="text-center space-y-4">
          <div className="inline-flex items-center justify-center p-3 bg-white/5 rounded-2xl mb-4 border border-white/10 shadow-2xl backdrop-blur-sm">
            <Calculator className="w-8 h-8 text-primary" />
          </div>
          <h1 className="text-5xl font-extrabold tracking-tight bg-gradient-to-br from-white to-white/40 bg-clip-text text-transparent drop-shadow-sm">
            Cryptic Solver
          </h1>
          <p className="text-lg text-muted-foreground/80 max-w-2xl mx-auto font-light">
            Blazing fast constraint satisfaction algorithms resolving arithmetic puzzles where letters represent unique digits.
          </p>
        </div>

        <Card className="glass border-white/10 shadow-2xl overflow-hidden bg-black/40 backdrop-blur-xl">
          <CardHeader className="space-y-1 pb-6 border-b border-white/5">
            <CardTitle className="text-2xl font-bold flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-primary" />
              Intelligence Core
            </CardTitle>
            <CardDescription className="text-zinc-400">
              Enter any valid cryptarithmetic equation or select an example.
            </CardDescription>
          </CardHeader>
          <CardContent className="pt-6 space-y-6">
            <div className="flex flex-col sm:flex-row gap-4">
              <Input 
                type="text" 
                value={equation} 
                onChange={(e) => setEquation(e.target.value)} 
                className="text-xl py-6 font-mono bg-zinc-950/50 border-zinc-800 focus-visible:ring-primary/50 placeholder:text-zinc-700"
                placeholder="e.g. SEND + MORE = MONEY"
                onKeyDown={(e) => e.key === 'Enter' && handleSolve()}
              />
              <Button 
                size="lg" 
                className="py-6 px-8 text-lg font-semibold bg-primary hover:bg-primary/90 transition-all shadow-[0_0_20px_rgba(var(--primary),0.3)] hover:shadow-[0_0_30px_rgba(var(--primary),0.5)]"
                onClick={handleSolve}
                disabled={isSolving || !equation}
              >
                {isSolving ? (
                  <span className="flex items-center gap-2">
                    <span className="w-5 h-5 border-2 border-white/30 border-t-white rounded-full animate-spin" />
                    Solving...
                  </span>
                ) : (
                  <span className="flex items-center gap-2">
                    <Play className="w-5 h-5 fill-current" />
                    Compute
                  </span>
                )}
              </Button>
            </div>

            <div className="flex flex-wrap gap-2 pt-2">
              <span className="text-sm text-zinc-500 py-1 mr-2">Examples:</span>
              {EXAMPLES.map((ex) => (
                <Badge 
                  key={ex} 
                  variant="secondary" 
                  className="cursor-pointer hover:bg-primary/20 hover:text-primary transition-colors bg-white/5 text-zinc-300 font-mono"
                  onClick={() => {
                    setEquation(ex);
                  }}
                >
                  {ex}
                </Badge>
              ))}
            </div>
          </CardContent>
        </Card>

        {error && (
          <div className="animate-in fade-in slide-in-from-top-4 duration-500">
            <Card className="border-red-500/20 bg-red-500/10 backdrop-blur-md">
              <CardContent className="flex items-center gap-3 py-4 text-red-400">
                <AlertCircle className="w-5 h-5 flex-shrink-0" />
                <p className="font-medium">{error}</p>
              </CardContent>
            </Card>
          </div>
        )}

        {solutions !== null && !error && (
          <div className="space-y-6 animate-in fade-in slide-in-from-bottom-8 duration-700">
            <div className="flex items-center justify-between">
              <h2 className="text-2xl font-semibold flex items-center gap-2">
                {solutions.length === 0 ? (
                  <span className="text-zinc-400">No Solutions Found</span>
                ) : (
                  <>
                    <CheckCircle2 className="w-6 h-6 text-green-400" />
                    <span className="text-green-50">{solutions.length} Solution{solutions.length !== 1 ? 's' : ''} Found</span>
                  </>
                )}
              </h2>
              <span className="text-sm font-mono text-zinc-500 px-3 py-1 bg-white/5 rounded-full border border-white/10">
                Resolved in {solveTime}ms
              </span>
            </div>

            {solutions.map((sol, index) => (
              <Card key={index} className="glass border-white/10 overflow-hidden relative group">
                <div className="absolute top-0 left-0 w-1 h-full bg-primary/50 group-hover:bg-primary transition-colors" />
                <CardHeader className="bg-white/5 border-b border-white/5 py-4">
                  <CardTitle className="text-lg font-mono text-zinc-200">
                    Solution #{index + 1}
                  </CardTitle>
                </CardHeader>
                <CardContent className="grid md:grid-cols-2 gap-8 p-6">
                  <div className="space-y-4">
                    <h3 className="text-sm font-medium text-zinc-500 uppercase tracking-wider">Letter Mappings</h3>
                    <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
                      {Object.entries(sol.mapping).sort().map(([letter, digit]) => (
                        <div key={letter} className="flex items-center justify-between p-3 rounded-xl bg-zinc-900/80 border border-white/5 font-mono">
                          <span className="text-primary font-bold text-lg">{letter}</span>
                          <ArrowRight className="w-4 h-4 text-zinc-600" />
                          <span className="text-zinc-100 font-bold text-lg">{digit}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                  
                  <div className="space-y-4">
                    <h3 className="text-sm font-medium text-zinc-500 uppercase tracking-wider">Arithmetic Verification</h3>
                    <div className="p-5 rounded-xl bg-zinc-900/80 border border-white/5 space-y-3 font-mono text-zinc-300 relative overflow-hidden">
                      <div className="absolute top-0 right-0 p-4 opacity-5 pointer-events-none">
                        <Calculator className="w-24 h-24" />
                      </div>
                      
                      {sol.details.operand_strings.map((str, i) => (
                        <div key={i} className="flex justify-between items-center text-lg z-10 relative">
                          <span className="text-zinc-500">{str.split('=')[0].trim()}</span>
                          <span className="text-zinc-100 font-bold">{str.split('=')[1].trim()}</span>
                        </div>
                      ))}
                      <div className="h-px bg-white/10 w-full my-3" />
                      <div className="flex justify-between items-center text-xl text-primary z-10 relative">
                        <span>{equation.split('=')[1].trim()}</span>
                        <span className="font-bold">{sol.details.result_value}</span>
                      </div>
                    </div>
                    
                    <div className="w-full text-center p-3 rounded-lg bg-primary/10 border border-primary/20 text-primary font-mono text-sm shadow-inner">
                      {sol.details.equation}
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        )}
      </div>

      <div className="mt-auto pt-16 pb-4 w-full text-center z-10 animate-in fade-in duration-1000">
        <p className="text-zinc-500 text-sm font-mono tracking-widest uppercase">
          Made by <span className="text-primary font-semibold">Muhammed Aflah S</span>
        </p>
      </div>
    </main>
  );
}
